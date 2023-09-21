# IoC

You may have seen this thing called `IoC`. What is this mysterious and hard to type acronym? You've come to the right place.

# What is IoC?
IoC stands for *Inversion of Control*. What our `IoCManager` does is more specifically *Dependency Injection*. At it's core, Dependency Injection means that instead of saying "I want this specific log manager", you just say "I want a thing that can log messages for me".

How does this work? C# interfaces! In the above example, you wouldn't refer to a static `LogManager`, instead you would tell IoC to fetch *anything* that implements `ILogManager` for you to use. This creates cleaner, easier to test and more maintainable code.

The system is quite simple to use as long as you know what the gist of it is (why you're reading this!), so don't worry.

# How do I use it?
First of all, the `IoCManager` is `static` so you can use it from anywhere. 

There's two real parts to using IoC. *Making* a dependency, and *getting* one. When talking about IoC, a "dependency" is something that it manages. 

## Registering a dependency.

All the dependencies are manually registered at the start of the program, this means `Program.cs` for client and server, and `SS14UnitTest.cs` for the unit testing project. IoC maps a type, usually an interface, to a concrete implementation it can instantiate. A concrete implementation can have multiple interfaces, but an interface can have only one implementation. This is done through the `Register<TInterface, TImplementation>(bool overwrite = false)` where `TImplementation : class, TInterface, new()` method on the IoC Manager. What this basically means is that you pass it two types, the second one will be spawned but must inherit or implement the first. Where these types are registered depends on whether you're in content/server/client etc but it's all single organized places. `ClientIoC.cs` (engine), `ClientContentIoC.cs`, etc... You should be able to pick up on the pattern.

So, **to make a dependency**, you're gonna want two things: an interface, and an implementation. It's common to simply name the interface the same as the implementation, but with an `I` preprended following C# convention. So, if I were to make a new dependency on the server, I would do this:


```cs
// Content.Server/Example/MyDependency.cs
namespace Content.Server.Example
{
    public class MyDependency : IMyDependency
    {
        public void Foo()
        {
            Console.WriteLine("Hello World!");
        }
    }
}

// Content.Server/Interfaces/Example/IMyDependency.cs
namespace Content.Server.Interfaces.Example
{
    public interface IMyDependency
    {
        /// <summary>
        /// Writes a message to the console.
        /// </summary>
        void Foo();
    }
}

// ServerContentIoC.cs
IoCManager.Register<IMyDependency, MyDependency>();
```

And you have made your dependency available to the world. Now how do you retrieve it? Simple!

## Retrieving a dependency.

The most simple way of retrieving a dependency is to use `IoCManager.Resolve<T>`, where `T` is the interface used in the `Register<>` call. In our above example, `Resolve<IMyDependency>()` would return an instance of `MyDependency`, and this instance will always be the same one and shared throughout the entire program.

So, say our example wants to log when `Foo()` gets called. Simple!

```cs
public class MyDependency : IMyDependency
{
    public void Foo()
    {
        ILogger logger = IoCManager.Resolve<ILogger>();
        logger.info("Hi!");
        Console.WriteLine("Hello World!");
    }
}
```

Simple as that.

This however is not pretty. It's kind of a pain and it has a severe issue of circular dependencies, also, the method doesn't even work inside the constructors of dependencies. There's a solution of course: 

### Field Injection and You

To solve the issues with `Resolve<T>`, the IoC Manager can "inject" dependencies into fields. This means that two dependencies can reference each other without issue. Using it is also quite simple. The IoC Manager finds all fields marked with the `[Dependency]` attribute (completely ignoring `readonly` and `private`), and resolves the field's type. This is done after the constructors of all dependencies are ran. After the fields are injected, if your dependency implements `IPostInjectInit`, `IPostInjectInit.PostInject()` will be called, if you need to communicate with your dependencies. Note that most of the time you should still have an explicit initialization call somewhere, as this "pseudo-constructor" is prone to race conditions.

So to take our example from above. Let's convert it to our superior method. We'll also add a log message whenever the type gets instantiated, **though you should refrain from doing this in practice**:

```cs
public class MyDependency : IMyDependency, IPostInjectInit
{
    [Dependency]
    private readonly ILogger logger = default!;

    // Gets called when logger becomes available.
    public void PostInject()
    {
        logger.info("MyDependency being created!");
        // IMPORTANT: Don't actually do this specific thing with a logger. It gets the point across but is broken.
        // Because logger won't have been initialized properly yet, it has no output file.
        // As such, this message will go to the console, but will not be logged to any files. This is a bug.
    }

    public void Foo()
    {
        // This is fine of course, provided `Foo()` gets called after `BaseServer` had its way setting things up.
        logger.info("Hi!");
        Console.WriteLine("Hello World!");
    }
}
```

Field injection can be ran manually by using `IoCManager.InjectDependencies(object)`. It is done automatically for many dynamically instantiated types, such as entity components, entity systems, and anything instantiated via `IDynamicTypeFactory`.